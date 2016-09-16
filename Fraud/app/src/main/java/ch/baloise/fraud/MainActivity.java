package ch.baloise.fraud;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    private final static String TAG = "MainActivity";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Get reference of button
        Button btn = (Button)findViewById(R.id.schadensmeldung);
        if(btn == null){
            Log.e(TAG, "Could not retrieve a reference to the button \"Schadensmeldung\".");
            finish();
            return;
        }

        // register callback
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, LossReportActivity.class);
                startActivity(intent);
            }
        });
    }
}
