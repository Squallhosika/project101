package com.unicorn.userui;

import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.util.List;

/**
 * Created by Keuvin on 21/09/2017.
 */

public class HomeAdapter extends RecyclerView.Adapter<HomeAdapter.ViewHolder>{
    private List<String> values;

    public HomeAdapter(List<String> values) {
        this.values = values;
    }

    @Override
    public HomeAdapter.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View v = inflater.inflate(R.layout.test_list_item, parent, false);

        ViewHolder viewHolder = new ViewHolder(v);
        return viewHolder;
    }

    @Override
    public void onBindViewHolder(HomeAdapter.ViewHolder holder, int position) {
        final String name = values.get(position);
        holder.tvFirstLine.setText(name);
        holder.tvFirstLine.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                System.out.println("test");
            }
        });
        holder.tvSecondLine.setText("Second line: " + name);

    }

    @Override
    public int getItemCount() {
        return values.size();
    }


    public class ViewHolder extends RecyclerView.ViewHolder {
        public TextView tvFirstLine;
        public TextView tvSecondLine;

        public ViewHolder(View itemView) {
            super(itemView);
            tvFirstLine = (TextView) itemView.findViewById(R.id.firstLine);
            tvSecondLine = (TextView) itemView.findViewById(R.id.secondLine);
        }
    }
}
