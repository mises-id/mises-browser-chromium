package org.chromium.chrome.browser.settings;
import androidx.preference.PreferenceFragmentCompat;
import android.os.Bundle;
import android.app.Activity;

public class ToolbarSettings extends PreferenceFragmentCompat {
	        public ToolbarSettings() {
			setHasOptionsMenu(true);		  
		}
		public static void AskForRelaunch(Activity activity) {}
		@Override
		public void onCreatePreferences(Bundle savedInstanceState, String rootKey) {
		}
}
