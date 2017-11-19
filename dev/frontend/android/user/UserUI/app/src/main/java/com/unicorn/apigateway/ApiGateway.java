package com.unicorn.apigateway;

import com.unicorn.apigateway.model.Basket;
import com.unicorn.apigateway.model.Client;
import com.unicorn.apigateway.model.Item;
import com.unicorn.apigateway.model.Order;
import com.unicorn.apigateway.model.OrderLine;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by jonathan on 23/10/17.
 */

public class ApiGateway {

    private static int orderCounter = 0;
    private static List<Order> orders = new ArrayList<>();

    public static Object  call(String function, Object data){
        if (function.equals("getClients")) {
            return getClients();
        } else if (function.equals("getItems")) {
            return getItems();
        } else if (function.equals("getOrders")) {
            return getOrders(data);
        } else if (function.equals("getMenu")) {
            return getMenu(data);
        } else if (function.equals("getOrder")) {
            return getOrder(data);
        } else if (function.equals("getItem")) {
            return getItem(data);
        } else if (function.equals("getBasket")) {
            return getBasket(data);
        } else if (function.equals("createOrder")) {
            return createOrder(data);
        }


        return null;
    }

    private static List<Client> getClients(){

        List<Client> clients = new ArrayList<>();
        Client client = null;
        for (int k=0; k<100; k++){
            client = new Client(""+k, "Client " + k, "Description client " + k);
            clients.add(client);
        }

        return clients;
    }

    private static List<Item> getItems(){

        List<Item> items = new ArrayList<>();
        Item item = null;
        for (int k=0; k<100; k++){
            item = new Item(""+k, "Item " + k, "Description item " + k);
            items.add(item);
        }

        return items;
    }

    private static Basket getMenu(Object clientId){

        List<OrderLine> items = new ArrayList<>();
        int id = Integer.parseInt((String) clientId);
        for (int k=0; k< 100; k++){
            if (k%10== id ){
                items.add(new OrderLine(new Item(""+k, "Item " + k, "Description item " + k), 0.5 + k, 0));
            }
        }

        return new Basket(Integer.toString(id), items);
    }

    private static List<Order> getOrders(Object data){
        return orders;
    }

    private static Order getOrder(Object orderId){
        String strId = (String) orderId;
        for (Order order: orders) {
            if ( strId.equals(order.getId())){
                return order;
            }
        }
        return null;
    }

    private static Basket getBasket(Object menuId){
        List<OrderLine> orderLines = new ArrayList<OrderLine>();

        Item item = null;
        for (int k=0; k<4; k++){
            item = new Item(""+k, "Item " + k, "Description item " + k);
            orderLines.add(new OrderLine(item, 1.2 * k + 0.5, k + 1));
        }

        return new Basket((String) menuId, orderLines);
    }

    private static Order createOrder(Object basket){
        Order order = new Order(Integer.toString(++orderCounter), (Basket) basket);
        orders.add(order);
        return order;
    }

    private static Item getItem(Object itemId){
        return new Item(""+itemId, "Item " + itemId, "Description item " + itemId);
    }


    public static void main(String[] args) {
        System.out.println(ApiGateway.getMenu(1));
        System.out.println(ApiGateway.getMenu(2));
        System.out.println(ApiGateway.getMenu(3));
    }
}
