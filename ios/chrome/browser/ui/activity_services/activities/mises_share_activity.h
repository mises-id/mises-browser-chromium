// Copyright 2020 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef IOS_CHROME_BROWSER_UI_ACTIVITY_SERVICES_ACTIVITIES_MISES_SHARE_ACTIVITY_H_
#define IOS_CHROME_BROWSER_UI_ACTIVITY_SERVICES_ACTIVITIES_MISES_SHARE_ACTIVITY_H_

#import <UIKit/UIKit.h>

#import "ios/chrome/browser/ui/commands/mises_share_commands.h"
#include "url/gurl.h"

@interface MisesShareActivity : UIActivity

- (instancetype)initWithURL:(const GURL&)activityURL
                      title:(NSString*)title
                    handler:(id<MisesShareCommands>)handler
    NS_DESIGNATED_INITIALIZER;

- (instancetype)init NS_UNAVAILABLE;

@end

#endif  // IOS_CHROME_BROWSER_UI_ACTIVITY_SERVICES_ACTIVITIES_MISES_SHARE_ACTIVITY_H_
