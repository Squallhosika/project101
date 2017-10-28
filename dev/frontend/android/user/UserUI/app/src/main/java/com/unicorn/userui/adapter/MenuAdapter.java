package com.unicorn.userui.adapter;

import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.unicorn.apigateway.model.Item;
import com.unicorn.userui.R;

import java.util.List;

/**
 * Created by jonathan on 23/10/17.
 */

public class MenuAdapter extends RecyclerView.Adapter<MenuAdapter.ViewHolder>{

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
        final String name = items.get(position).getName();
        final String description = items.get(position).getDescription();


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
        public TextView tvItemName;
        public TextView tvItemDescription;

        public ViewHolder(View itemView) {
            super(itemView);
            tvItemName = (TextView) itemView.findViewById(R.id.item_name);
            tvItemDescription = (TextView) itemView.findViewById(R.id.item_description);
        }
    }
}
