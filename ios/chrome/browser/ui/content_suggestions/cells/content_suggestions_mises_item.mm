// Copyright 2017 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#import "ios/chrome/browser/ui/content_suggestions/cells/content_suggestions_mises_item.h"

#import <MaterialComponents/MaterialTypography.h>

#include "base/check_op.h"
#import "ios/chrome/browser/ui/util/uikit_ui_util.h"
#include "ios/chrome/common/string_util.h"
#import "ios/chrome/common/ui/colors/semantic_color_names.h"
#import "ios/chrome/common/ui/util/constraints_ui_util.h"


#if !defined(__has_feature) || !__has_feature(objc_arc)
#error "This file requires ARC support."
#endif

namespace {

const CGFloat kLabelMargin = 14;
//const CGFloat kLabelLineSpacing = 4;
const CGFloat kLabelIconMargin = 8;
const CGFloat kDescFontSize = 15;
const CGFloat kWelcomeFontSize = 25;
const CGFloat kButtonHeight = 50;
const CGFloat kIconHeight = 55;
const CGFloat kIconWidth = 89;
const CGFloat kIconTopMargin = 10;
NSString * const kWelcomeText = @"Welcome to Mises!";
NSString * const kDescText = @"Mises is a blockchain which aims to support decentralized ID, strorage & social media. ";
NSString * const kButtonTitle = @"Enter Mises";
NSURL * const kLink = [NSURL URLWithString:@"https://home.mises.site/"];
}  // namespace

#pragma mark - ContentSuggestionsMisesItem

@implementation ContentSuggestionsMisesItem

@synthesize suggestionIdentifier = _suggestionIdentifier;
@synthesize metricsRecorded = _metricsRecorded;

- (instancetype)initWithType:(NSInteger)type {
  self = [super initWithType:type];
  if (self) {
    self.cellClass = [ContentSuggestionsMisesCell class];
  }
  return self;
}

- (void)configureCell:(ContentSuggestionsMisesCell*)cell {
  [super configureCell:cell];
  cell.accessibilityIdentifier = [[self class] accessibilityIdentifier];
}

- (CGFloat)cellHeightForWidth:(CGFloat)width {
  return [self.cellClass heightForWidth:width];
}

+ (NSString*)accessibilityIdentifier {
  return @"ContentSuggestionsMisesIdentifier";
}

@end

#pragma mark - ContentSuggestionsMisesCell

@interface ContentSuggestionsMisesCell ()

@property(nonatomic, strong) UIImageView* iconView;
@property(nonatomic, strong) UILabel* welcomeLabel;
@property(nonatomic, strong) UILabel* descLabel;
@property(nonatomic, strong) UIView* containerView;

@end

@implementation ContentSuggestionsMisesCell

@synthesize iconView = _iconView;
@synthesize welcomeLabel = _welcomeLabel;
@synthesize descLabel = _descLabel;
@synthesize containerView = _containerView;
@synthesize enterButton = _enterButton;

- (instancetype)initWithFrame:(CGRect)frame {
  self = [super initWithFrame:frame];
  if (self) {
    _iconView =  [[UIImageView alloc]
        initWithImage:[UIImage imageNamed:@"mises_welcome"]];
    _welcomeLabel = [[UILabel alloc] init];
    _descLabel = [[UILabel alloc] init];
    _containerView = [[UIView alloc] init];
    _enterButton = [[MDCButton alloc] init];

    _iconView.translatesAutoresizingMaskIntoConstraints = NO;
    _welcomeLabel.translatesAutoresizingMaskIntoConstraints = NO;
    _containerView.translatesAutoresizingMaskIntoConstraints = NO;
    _descLabel.translatesAutoresizingMaskIntoConstraints = NO;
    _enterButton.translatesAutoresizingMaskIntoConstraints = NO;
      
    [[self class] configureWelcomeLabel:self.welcomeLabel withText:kWelcomeText];
    [[self class] configureDescLabel:self.descLabel withText:kDescText];
      
      _iconView.contentMode = UIViewContentModeScaleAspectFit;
    [_enterButton setTitle:kButtonTitle forState:UIControlStateNormal];
    [_enterButton setBackgroundColor:UIColorFromRGB(0x5D61FF)];
    _enterButton.layer.cornerRadius = kButtonHeight / 2;

    [self.contentView addSubview:_containerView];
    [_containerView addSubview:_iconView];
    [_containerView addSubview:_welcomeLabel];
    [_containerView addSubview:_descLabel];
    [_containerView addSubview:_enterButton];

    ApplyVisualConstraintsWithMetrics(
        @[
          @"V:|-(>=margin)-[icon(iconHeight)]-(margin)-[welcome]-(margin)-[desc]-(margin)-[enter(buttonHeight)]-(>=margin)-|",
          @"V:|[container]|", @"H:|[icon]|", @"H:|[welcome]|",
          @"H:|[desc]|",@"H:|-(>=margin)-[enter]-(>=margin)-|",
          @"H:|->=0-[container]->=0-|"
        ],
        @{
          @"icon" : _iconView,
          @"welcome" : _welcomeLabel,
          @"desc" : _descLabel,
          @"enter" : _enterButton,
          @"container" : _containerView
        },
        @{
          @"margin" : @(kLabelMargin),
          @"iconMargin" : @(kIconTopMargin),
          @"buttonHeight" : @(kButtonHeight),
          
          @"iconHeight" : @(kIconHeight),
          @"iconWidth" : @(kIconWidth),
          @"spacing" : @(kLabelIconMargin)
        });
    [NSLayoutConstraint activateConstraints:@[
      [_containerView.centerXAnchor
          constraintEqualToAnchor:self.contentView.centerXAnchor]
    ]];
      [NSLayoutConstraint activateConstraints:@[
        [_enterButton.centerXAnchor
            constraintEqualToAnchor:_containerView.centerXAnchor]
      ]];
  }
  return self;
}

+ (CGFloat)heightForWidth:(CGFloat)width {
  UILabel* label1 = [[UILabel alloc] init];
  [self configureWelcomeLabel:label1 withText:kWelcomeText];
  UILabel* label2 = [[UILabel alloc] init];
  [self configureDescLabel:label2 withText:kDescText];
  CGSize sizeForLabel = CGSizeMake(width, 500);

  return 5 * kLabelMargin + [label1 sizeThatFits:sizeForLabel].height + kButtonHeight + [label2 sizeThatFits:sizeForLabel].height + kIconHeight;
}


#pragma mark UIView

// Implements -layoutSubviews as per instructions in documentation for
// +[MDCCollectionViewCell cr_preferredHeightForWidth:forItem:].
- (void)layoutSubviews {
  [super layoutSubviews];

  // Adjust the text label preferredMaxLayoutWidth when the parent's width
  // changes, for instance on screen rotation.
  CGFloat parentWidth = CGRectGetWidth(self.contentView.bounds);

  self.welcomeLabel.preferredMaxLayoutWidth = parentWidth;
  self.descLabel.preferredMaxLayoutWidth = parentWidth;

  // Re-layout with the new preferred width to allow the label to adjust its
  // height.
  [super layoutSubviews];
}

#pragma mark Private

// Configures the |promoLabel| with the |text|.
+ (void)configureWelcomeLabel:(UILabel*)label withText:(NSString*)text {
  label.font =
      [[MDCTypography fontLoader] regularFontOfSize:kWelcomeFontSize];
  label.textColor = [UIColor colorNamed:kTextPrimaryColor];
  label.numberOfLines = 0;
    label.textAlignment = NSTextAlignmentCenter;
  [label setText:[NSString stringWithString:text]];

}

+ (void)configureDescLabel:(UILabel*)label withText:(NSString*)text {
  label.font =
      [[MDCTypography fontLoader] regularFontOfSize:kDescFontSize];
  label.textColor = [UIColor colorNamed:kTextPrimaryColor];
  label.numberOfLines = 0;
  [label setText:[NSString stringWithString:text]];

}

@end
