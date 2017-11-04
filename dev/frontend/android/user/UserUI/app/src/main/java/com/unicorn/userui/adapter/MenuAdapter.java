package com.unicorn.userui.adapter;

import android.content.Context;
import android.content.Intent;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.unicorn.apigateway.model.Item;
import com.unicorn.userui.R;
import com.unicorn.userui.activity.ItemCardActivity;
import com.unicorn.userui.activity.MenuActivity;

import java.util.List;

/**
 * Created by jonathan on 23/10/17.
 */

public class MenuAdapter extends RecyclerView.Adapter<MenuAdapter.ViewHolder>{

    private Context mContext;
    private List<Item> items;

    public MenuAdapter(List<Item> items) {
        this.items = items;
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View v = inflater.inflate(R.layout.rv_menu_item, parent, false);

        ViewHolder viewHolder = new ViewHolder(v);
        return viewHolder;
    }

    @Override
    public void onBindViewHolder(ViewHolder holder, int position) {
        final String id = items.get(position).getId();
        final String name = items.get(position).getName();
        final String description = items.get(position).getDescription();


        holder.tvItemId.setText(id);
        holder.tvItemName.setText(name);
//        holder.tvOrderName.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                System.out.println("test");
//            }
//        });
//
        holder.tvItemDescription.setText(description);

    }

    @Override
    public int getItemCount() {
        return items.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        public TextView tvItemId;
        public TextView tvItemName;
        public TextView tvItemDescription;

        public ViewHolder(View itemView) {
            super(itemView);
            tvItemId = (TextView) itemView.findViewById(R.id.item_id);
            tvItemName = (TextView) itemView.findViewById(R.id.item_name);
            tvItemDescription = (TextView) itemView.findViewById(R.id.item_description);

            mContext = itemView.getContext();

            itemView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    openItemCard(tvItemId.getText().toString());
                }
            });
        }
    }

    private void openItemCard(String itemId) {
        Intent intent = new Intent(mContext, ItemCardActivity.class);
        intent.putExtra("itemId", itemId);
        mContext.startActivity(intent);
    }
}
