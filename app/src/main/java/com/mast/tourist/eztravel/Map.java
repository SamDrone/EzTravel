package com.mast.tourist.eztravel;

import android.os.Bundle;
import android.support.v4.app.FragmentActivity;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

import java.util.Random;

public class Map extends FragmentActivity implements OnMapReadyCallback {

    private GoogleMap mMap;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_map);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);
    }
    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;
        final int min = 0;
        final int max = 5;
        int n=5;
        final int random = new Random().nextInt(n);
        if(random==0){
            LatLng FireWood = new LatLng(26.888589, 75.808142);
            mMap.addMarker(new MarkerOptions().position(FireWood).title("The FireWood"));
            mMap.moveCamera(CameraUpdateFactory.newLatLng(FireWood));
        if(random==1){
            LatLng Doorbeen = new LatLng(26.8879476, 75.803310099);
            mMap.addMarker(new MarkerOptions().position(Doorbeen).title("Doorbeen"));
            mMap.moveCamera(CameraUpdateFactory.newLatLng(Doorbeen));
        }
        if(random==2){
            LatLng Dragon = new LatLng(26.919676, 75.794768);
            mMap.addMarker(new MarkerOptions().position(Dragon).title("The Dragon"));
            mMap.moveCamera(CameraUpdateFactory.newLatLng(Dragon));
        }
        if(random==3){
            LatLng Suvarna = new LatLng(26.898284, 75.808433);
            mMap.addMarker(new MarkerOptions().position(Suvarna).title("Suvarna"));
            mMap.moveCamera(CameraUpdateFactory.newLatLng(Suvarna));
        }
        if(random==4){
            LatLng CourtYard = new LatLng(26.891823, 75.806495);
            mMap.addMarker(new MarkerOptions().position(CourtYard).title("The CourtYard"));
            mMap.moveCamera(CameraUpdateFactory.newLatLng(CourtYard));
        }
    }}
}