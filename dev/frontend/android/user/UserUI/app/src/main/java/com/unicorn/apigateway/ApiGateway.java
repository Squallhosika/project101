package com.unicorn.apigateway;

import com.unicorn.apigateway.model.Client;
import com.unicorn.apigateway.model.Item;
import com.unicorn.apigateway.model.Order;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by jonathan on 23/10/17.
 */

public class ApiGateway {

    public static Object  call(String function, Object data){
        if (function.equals("getClients")){
            return getClients();

        } else if (function.equals("getItems")){
            return getItems();
        }
         else if (function.equals("getOrders")){
            return getOrders();
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

    private static List<Order> getOrders(){

        List<Order> orders = new ArrayList<>();
        Order order = null;
        for (int k=0; k<100; k++){
            order = new Order(""+k, "Order " + k, "Description order " + k);
            orders.add(order);
        }

        return orders;
    }

}
