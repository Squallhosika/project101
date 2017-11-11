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

    public void addItem(Item item) {
        OrderLine orderLine = getOrderLine(item);
        if (orderLine != null) {
            orderLine.addOne();
        }
        else {
            orderLine = new OrderLine(item, 1, 1);
            orderLines.add(orderLine);
        }
    }

    public void removeItem(Item item){
        OrderLine orderLine = getOrderLine(item);
        if(orderLine != null){
            if(orderLine.getQuantity() == 1)
            {
                orderLines.remove(orderLine);
            }
            else
            {
                orderLine.removeOne();
            }
        }
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

}

