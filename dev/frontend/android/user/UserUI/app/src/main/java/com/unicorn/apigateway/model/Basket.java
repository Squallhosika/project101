package com.unicorn.apigateway.model;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by jonathan on 23/10/17.
 */
public class Basket implements Serializable {

    private final String menuId;
    private List<OrderLine> orderLines;


    public Basket(String menuId, List<OrderLine> orderLines) {
        this.menuId = menuId;
        this.orderLines = orderLines;
    }

    public Basket(String menuId) {
        this.menuId = menuId;
        this.orderLines = new ArrayList<>();
    }

    public String getMenuId() {
        return menuId;
    }

    public List<OrderLine> getOrderLines() {
        return orderLines;
    }

    public void addItem(Item item) {
        OrderLine orderLine = new OrderLine(item, 1, 1);
        orderLines.add(orderLine);
    }



}

