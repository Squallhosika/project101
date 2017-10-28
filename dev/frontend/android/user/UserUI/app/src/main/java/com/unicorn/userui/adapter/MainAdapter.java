package com.unicorn.userui.adapter;

import android.content.Context;
import android.content.Intent;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;


import com.unicorn.apigateway.model.Client;
import com.unicorn.userui.R;
import com.unicorn.userui.activity.MainActivity;
import com.unicorn.userui.activity.MenuActivity;

import java.util.List;

/**
 * Created by jonathan on 23/10/17.
 */

public class MainAdapter extends RecyclerView.Adapter<MainAdapter.ViewHolder> {

    private Context mContext;
    private List<Client> clients;

    public MainAdapter(List<Client> clients) {
        this.clients = clients;
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View v = inflater.inflate(R.layout.rv_main_client, parent, false);

        ViewHolder viewHolder = new ViewHolder(v);
        return viewHolder;
    }



    @Override
    public void onBindViewHolder(ViewHolder holder, int position) {
        final String id = clients.get(position).getId();
        final String name = clients.get(position).getName();
        final String description = clients.get(position).getDescription();

        holder.tvClientId.setText(id);

        holder.tvClientName.setText(name);
//        holder.tvOrderName.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                System.out.println("test");
//            }
//        });
//
        holder.tvClientDescription.setText(description);

    }

    @Override
    public int getItemCount() {
        return clients.size();
    }


    private void openMenu(String clientId) {
        Intent intent = new Intent(mContext, MenuActivity.class);
        intent.putExtra("clientId", clientId);
        mContext.startActivity(intent);
    }



    public class ViewHolder extends RecyclerView.ViewHolder {
        public TextView tvClientId;
        public TextView tvClientName;
        public TextView tvClientDescription;

        public ViewHolder(View itemView) {
            super(itemView);

            tvClientId = (TextView) itemView.findViewById(R.id.client_id);
            tvClientName = (TextView) itemView.findViewById(R.id.client_name);
            tvClientDescription = (TextView) itemView.findViewById(R.id.client_description);

            mContext = itemView.getContext();

            itemView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    openMenu(tvClientId.getText().toString());
                }
            });
        }
    }
}
