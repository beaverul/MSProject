using Android.App;
using Android.Widget;
using Android.OS;
using Firebase.Xamarin.Database;

namespace SmartAlarmClock
{
    [Activity(Label = "SmartAlarmClock", MainLauncher = true, Icon = "@drawable/icon")]
    public class MainActivity : Activity
    {
        protected override void OnCreate(Bundle bundle)
        {
            base.OnCreate(bundle);
            this.UpdateUser("Alarmt0", "19:21.1", "Alarmd0", "05-29");
            // Set our view from the "main" layout resource
            // SetContentView (Resource.Layout.Main);
        }
        private async void UpdateUser(string alarmname, string alarmtime, string datename, string datetime)
        {
            var firebase = new FirebaseClient("https://smartalarmclock-5ad4f.firebaseio.com");
            await firebase.Child(alarmname).PutAsync(alarmtime);
            await firebase.Child(datename).PutAsync(datetime);

        }

    }
}

