package com.unicorn.userui.adapter;

import android.content.Context;
import android.content.Intent;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import com.unicorn.apigateway.model.Basket;
import com.unicorn.apigateway.model.Item;
import com.unicorn.userui.R;
import com.unicorn.userui.activity.ItemCardActivity;
import com.unicorn.userui.activity.MenuActivity;

import java.util.List;

/**
 * Created by jonathan on 23/10/17.
 */

public class MenuAdapter extends RecyclerView.Adapter<MenuAdapter.ViewHolder> {

    private Context mContext;
    private List<Item> items;
    private Basket basket;

    public MenuAdapter(List<Item> items, Basket basket) {
        this.items = items;
        this.basket = basket;
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
        public ImageView ivItemImage;
        public ImageView ivAddItem;
        public ImageView ivRemoveItem;
        public TextView tvItemId;
        public TextView tvItemName;
        public TextView tvItemDescription;

        public ViewHolder(View itemView) {
            super(itemView);
            ivItemImage = (ImageView) itemView.findViewById(R.id.item_image);
            tvItemId = (TextView) itemView.findViewById(R.id.item_id);
            tvItemName = (TextView) itemView.findViewById(R.id.item_name);
            tvItemDescription = (TextView) itemView.findViewById(R.id.item_description);
            ivAddItem = (ImageView) itemView.findViewById(R.id.btn_plus);
            ivRemoveItem = (ImageView) itemView.findViewById(R.id.btn_minus);
            mContext = itemView.getContext();

            ivItemImage.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    openItemCard(tvItemId.getText().toString());
                }
            });

            ivAddItem.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    String itemId = tvItemId.getText().toString();
                    String itemName = tvItemName.getText().toString();
                    String itemDescription = tvItemDescription.getText().toString();

                    Item item = new Item(itemId, itemName, itemDescription);
                    addItemToBasket(item);
                }
            });

            ivRemoveItem.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    String itemId = tvItemId.getText().toString();
                    String itemName = tvItemName.getText().toString();
                    String itemDescription = tvItemDescription.getText().toString();

                    Item item = new Item(itemId, itemName, itemDescription);
                    removeItemToBasket(item);
                }
            });
        }
    }

    private void addItemToBasket(Item item) {
        basket.addItem(item);
    }

    private void removeItemToBasket(Item item) {
        basket.removeItem(item);
    }

    private void openItemCard(String itemId) {
        Intent intent = new Intent(mContext, ItemCardActivity.class);
        intent.putExtra("itemId", itemId);
        mContext.startActivity(intent);
    }
}
