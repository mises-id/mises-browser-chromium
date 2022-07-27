// Copyright 2018 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#import "ios/chrome/browser/ui/toolbar/secondary_toolbar_coordinator.h"

#import "ios/chrome/browser/main/browser.h"
#import "ios/chrome/browser/ui/commands/application_commands.h"
#import "ios/chrome/browser/ui/commands/browser_commands.h"
#import "ios/chrome/browser/ui/commands/command_dispatcher.h"
#import "ios/chrome/browser/ui/toolbar/adaptive_toolbar_coordinator+subclassing.h"
#import "ios/chrome/browser/ui/toolbar/secondary_toolbar_view_controller.h"

#import "ios/chrome/browser/ui/favicon/favicon_attributes_provider.h"
#import "ios/chrome/browser/ui/favicon/favicon_attributes_with_payload.h"
#import "ios/chrome/browser/favicon/ios_chrome_large_icon_service_factory.h"


#import "ios/third_party/mises/mises_utils.h"

#import "net/base/mac/url_conversions.h"

#if !defined(__has_feature) || !__has_feature(objc_arc)
#error "This file requires ARC support."
#endif

namespace {

// Size of the favicon returned by the provider for the most visited items.
const CGFloat kAvatarFaviconSize = 128;
// Size below which the provider returns a colored tile instead of an image.
const CGFloat kAvatarFaviconMinimalSize = 64;

}  // namespace

@interface SecondaryToolbarCoordinator ()<MisesDelegate>
@property(nonatomic, strong) SecondaryToolbarViewController* viewController;
@property(nonatomic, strong) FaviconAttributesProvider* iconProvider;
@end

@implementation SecondaryToolbarCoordinator

@dynamic viewController;

#pragma mark - AdaptiveToolbarCoordinator

- (void)start {
  self.viewController = [[SecondaryToolbarViewController alloc] init];
  self.viewController.buttonFactory = [self buttonFactoryWithType:SECONDARY];
  // TODO(crbug.com/1045047): Use HandlerForProtocol after commands protocol
  // clean up.
  self.viewController.dispatcher =
      static_cast<id<ApplicationCommands, BrowserCommands>>(
          self.browser->GetCommandDispatcher());

  favicon::LargeIconService* largeIconService =
      IOSChromeLargeIconServiceFactory::GetForBrowserState(
          self.browser->GetBrowserState());;
  self.iconProvider = [[FaviconAttributesProvider alloc]
        initWithFaviconSize:kAvatarFaviconSize
             minFaviconSize:kAvatarFaviconMinimalSize
           largeIconService:largeIconService];

  [Mises setDelegate:self];
  [super start];
}
- (void)stop {
  [super stop];
  [Mises setDelegate:nil];
}
- (void)accountChanged {
  __weak SecondaryToolbarCoordinator* weakSelf = self;
  void (^completion)(FaviconAttributes*) = ^(FaviconAttributes* attributes) {
    SecondaryToolbarCoordinator* strongSelf = weakSelf;
    if (!strongSelf || !attributes) {
      return;
    }
    UIImage* image = attributes.faviconImage;
    [strongSelf.viewController updateMisesAvatar:image];
  };

  NSURL *nsurl = [NSURL URLWithString:[Mises misesAvatar]];
  if (nsurl) {
    GURL gurl = net::GURLWithNSURL(nsurl);

    [self.iconProvider fetchFaviconAttributesForURL:gurl completion:completion];
  }

}

@end
