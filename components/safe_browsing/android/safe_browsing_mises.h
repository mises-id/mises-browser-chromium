//
// Created by cg on 2023/1/3.
//

#ifndef COMPONENTS_SAFE_BROWSING_ANDROID_SAFE_BROWSING_MISES_H
#define COMPONENTS_SAFE_BROWSING_ANDROID_SAFE_BROWSING_MISES_H

#include <memory>
#include <string>
#include <vector>

#include "base/compiler_specific.h"
#include "base/memory/raw_ptr.h"
#include "base/memory/weak_ptr.h"
#include "services/network/public/cpp/shared_url_loader_factory.h"
#include "services/network/public/cpp/weak_wrapper_shared_url_loader_factory.h"
#include "services/network/test/test_url_loader_factory.h"
#include "chrome/browser/net/system_network_context_manager.h"

namespace network {
class SharedURLLoaderFactory;
class SimpleURLLoader;
}
// SafeBrowsing serving Mises.
class SafeBrowsingMises  {
 public:
  explicit SafeBrowsingMises();


 private:

  ~SafeBrowsingMises() override;

  void StartMisesURLCheck(const GURL& url);

  void OnURLLoadComplete(const network::SimpleURLLoader* source,
                         std::unique_ptr<std::string> response_body);

  scoped_refptr<network::SharedURLLoaderFactory> url_loader_factory_;

  std::unique_ptr<network::SimpleURLLoader> simple_url_loader_;

  GURL check_url_;

};


#endif  // COMPONENTS_SAFE_BROWSING_ANDROID_SAFE_BROWSING_MISES_H
