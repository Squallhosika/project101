package com.unicorn.userui;

import android.content.Intent;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.design.widget.NavigationView;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.support.v4.content.res.ResourcesCompat;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;

import com.unicorn.userui.api.HttpRequestTask;
import com.unicorn.userui.api.HttpRequestTaskAPI;

import java.util.Arrays;
import java.util.List;

public class MainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener, BottomNavigationView.OnNavigationItemSelectedListener {

    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
            = new BottomNavigationView.OnNavigationItemSelectedListener() {

        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {
//            mInflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
//            Fragment newFragment = new HomeFragment();
            FragmentManager fragmentManager = getSupportFragmentManager();
            switch (item.getItemId()) {
                case R.id.navigation_home:
//                    new HttpRequestTaskAPI(this, new HomeFragment()).execute();
//                    HomeFragment newFragment = new HomeFragment();
//                    HomeFragment newFragment = (HomeFragment) getSupportFragmentManager().findFragmentByTag(HomeFragment.class.getName());
//                    getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, newFragment).commit();
//
//                    HomeFragment newFragment = (HomeFragment) getSupportFragmentManager().findFragmentByTag(HomeFragment.class.getName());
//                    replaceFragment();
//                    getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, newFragment).commit();
//                    getSupportFragmentManager().findFragmentById(R.id.)


//                    inflater.inflate(R.layout.activity_main, parent, false);
//                    setContentView(R.layout.activity_main);
//                    fragment = new OrderFragment();
                    break;
//                    return true;
                case R.id.navigation_dashboard:
//                    Intent intent = new Intent(MainActivity.this, OrderFragment.class);
//                    startActivityFro(intent);
                    Fragment navFragment = new OrderFragment();
                    getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, navFragment).commit();
//                    setContentView(R.layout.content_main2);
//                    fragment = new OrderFragment();
                    break;
//                    return true;
                case R.id.navigation_notifications:
//                    Fragment notFragment = new TestFragment();
//                    getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, notFragment).commit();
                    break;
//                    return true;
            }
//            final FragmentTransaction transaction = fragmentManager.beginTransaction();
//            transaction.replace(R.id.content_main, fragment).commit();
            return true;
        }

    };


    private RecyclerView mRecyclerView;
    private HomeAdapter mAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        mRecyclerView = (RecyclerView) findViewById(R.id.rv_test);
        LinearLayoutManager layoutManager = new LinearLayoutManager(this, LinearLayoutManager.VERTICAL, false);
        mRecyclerView.setLayoutManager(layoutManager);
        mRecyclerView.setHasFixedSize(true);
//
        List<String> values = Arrays.asList("Android","IPhone","WindowsMobile","Blackberry",
                "WebOS","Ubuntu","Windows7","Max OS X","IPhone","WindowsMobile","Blackberry",
                "WebOS","Ubuntu","Windows7","Max OS X");
        mAdapter = new HomeAdapter(values);
        mRecyclerView.setAdapter(mAdapter);

        final Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        BottomNavigationView bottomNavigationView = (BottomNavigationView) findViewById(R.id.bottom_navigation);
        bottomNavigationView.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener);

        final DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);

        toggle.setDrawerIndicatorEnabled(false);
        Drawable drawable = ResourcesCompat.getDrawable(getResources(), R.drawable.ic_user_icon, getTheme());
        toggle.setHomeAsUpIndicator(drawable);
        toggle.setToolbarNavigationClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (drawer.isDrawerVisible(GravityCompat.START)) {
                    drawer.closeDrawer(GravityCompat.START);
                } else {
                    drawer.openDrawer(GravityCompat.START);
                }
            }
        });

        drawer.setDrawerListener(toggle);
        toggle.syncState();
//
//        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
//        navigationView.setNavigationItemSelectedListener(this);
//

//
//        new HttpRequestTaskAPI(this, new HomeFragment()).execute();
//        OrderFragment firstFragment = new OrderFragment();
//        HomeFragment firstFragment = new HomeFragment();
//        getSupportFragmentManager().beginTransaction().add(R.id.fragment_container, firstFragment).commit();


    }


//    public void replaceFragment(){
//        new HttpRequestTaskAPI(this, new HomeFragment()).execute();
////        getSupportFragmentManager().popBackStack(HomeFragment.class.getName(), 0);
//
////        HomeFragment fragment = (HomeFragment) getSupportFragmentManager().findFragmentByTag(HomeFragment.class.getName());
////        getSupportFragmentManager().findFragmentById(R.id.fragment_container);
////        getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, fragment).commit();
////        getSupportFragmentManager().executePendingTransactions();
//    }
//
//    public void addFragment(Fragment fragment) {
//        FragmentTransaction transaction = getSupportFragmentManager().beginTransaction();
//        transaction.add(R.id.fragment_container, fragment, fragment.getClass().getName());
//        transaction.addToBackStack(fragment.getClass().getName());
//        transaction.commit();
//        getSupportFragmentManager().executePendingTransactions();
//    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
//            new HttpRequestTask(this).execute();
//            new HttpRequestTaskAPI(this).execute();
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_camera) {
            // Handle the camera action
        } else if (id == R.id.nav_gallery) {


        } else if (id == R.id.nav_slideshow) {

        } else if (id == R.id.nav_manage) {

        } else if (id == R.id.nav_share) {

        } else if (id == R.id.nav_send) {

        }

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }


}
