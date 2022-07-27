// Copyright 2020 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#import "ios/chrome/browser/ui/activity_services/activities/mises_share_activity.h"

#include "base/metrics/user_metrics.h"
#include "base/metrics/user_metrics_action.h"
#include "ios/chrome/grit/ios_strings.h"
#include "ui/base/l10n/l10n_util_mac.h"

#if !defined(__has_feature) || !__has_feature(objc_arc)
#error "This file requires ARC support."
#endif

namespace {
NSString* const kMisesShareActivityType =
    @"com.google.chrome.MisesShareActivityType";
}  // namespace

@interface MisesShareActivity () {
  GURL _activityURL;
}

@property(nonatomic, weak, readonly) NSString* title;
@property(nonatomic, weak, readonly) id<MisesShareCommands> handler;

@end

@implementation MisesShareActivity

- (instancetype)initWithURL:(const GURL&)activityURL
                      title:(NSString*)title
                    handler:(id<MisesShareCommands>)handler {
  if (self = [super init]) {
    _activityURL = activityURL;
    _title = title;
    _handler = handler;
  }
  return self;
}

#pragma mark - UIActivity

- (NSString*)activityType {
  return kMisesShareActivityType;
}

- (NSString*)activityTitle {
  return l10n_util::GetNSString(IDS_IOS_SHARE_MENU_MISES_SHARE_ACTION);
}

- (UIImage*)activityImage {
  return [UIImage imageNamed:@"activity_services_mises_share"];
}

- (BOOL)canPerformWithActivityItems:(NSArray*)activityItems {
  return self.handler != nil;
}

+ (UIActivityCategory)activityCategory {
  return UIActivityCategoryAction;
}

- (void)performActivity {
  [self activityDidFinish:YES];
  [self.handler showMisesShare:_activityURL withImage:_activityURL withTitle:_title];
}

@end
