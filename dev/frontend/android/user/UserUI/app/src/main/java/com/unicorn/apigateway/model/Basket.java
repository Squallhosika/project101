package com.unicorn.apigateway.model;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

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

    public OrderLine addItem(Item item) {
        OrderLine line = getOrderLine(item);
        getOrderLine(item).addOne();
        return line;
    }

    public OrderLine removeItem(Item item){
        OrderLine orderLine = getOrderLine(item);
        if(orderLine.getQuantity() < 1) {
            orderLine.setQuanityZero();
        } else {
            orderLine.removeOne();
        }
        return orderLine;
    }

    private OrderLine getOrderLine(Item item){
        for (OrderLine line:orderLines) {
            if (line.getItem().getId().equals(item.getId())){
                return line;
            }
        }
        return null;
    }

    public double price() {
        double res = 0.0;
        for(OrderLine line : orderLines) {
            res += line.getPrice() * line.getQuantity();
        }
        return res;
    }

    public void resetQuantity() {
        for (OrderLine line : orderLines) {
            line.setQuanityZero();
        }
    }

    public Basket shrink() {
        List<OrderLine> shrinkLines = new ArrayList<OrderLine>();
        for (OrderLine line : orderLines) {
            if(line.getQuantity() > 0)
                shrinkLines.add(line.copy());
        }

        return new Basket(menuId, shrinkLines);
    }

}

