
// Copyright 2020 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef IOS_CHROME_BROWSER_UI_COMMANDS_MISES_SHARE_COMMANDS_H_
#define IOS_CHROME_BROWSER_UI_COMMANDS_MISES_SHARE_COMMANDS_H_

#import <Foundation/Foundation.h>

#include "url/gurl.h"

@protocol MisesShareCommands <NSObject>

- (void)showMisesShare:(const GURL&)link
	withImage:(const GURL&)image
        withTitle:(NSString*)title;
- (void)hideMisesShare;


@end

#endif  // IOS_CHROME_BROWSER_UI_COMMANDS_QR_GENERATION_COMMANDS_H_
