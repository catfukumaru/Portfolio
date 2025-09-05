import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;

public class MainFrame extends JFrame{
    final private Font mainFont = new Font("SansSerif", Font.BOLD, 18);
    
    JTextField add_item_field; //text field object
    JTextField delete_item_field;
    JTextField item_exits_field;
    JTextField rename_item_field;
    JTextField new_item_field;
    

    public static String item; // where the item to be replaced is kept
    
    ShoppingList s = new ShoppingList();
    
    public void initialize(){

        






        // -------------------------setting up the window, ie the the wooden posts------------------------
        setTitle("Temu Todoist");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //  set a close operation so the program exits when the window closes. or else it keeps runnig after you close the window
        setSize(500,600);
        setMinimumSize(new Dimension(300,400));
        
        
        
        


        // ------------------------ the functntions section at the centre -------------------
        // *************add item function********************************
        JLabel add_item = new JLabel("add_item"); //label object
        add_item.setFont(mainFont);
        add_item_field = new JTextField();
        add_item_field.setFont(mainFont);  
        add_item_field.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){
                String item = add_item_field.getText(); // what happens when the the text is added
                s.add_item(item);
                System.out.println("Item added: " + item);
                add_item_field.setText(""); // Clear field after
            }
        });  

        
         // *************delete item function********************************
        JLabel delete_item = new JLabel("delete_item"); //label object
        delete_item.setFont(mainFont);
        delete_item_field = new JTextField();
        delete_item_field.setFont(mainFont);  
        delete_item_field.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){
                String item = delete_item_field.getText(); // what happens when the the text is added
                s.delete_item(item);
                System.out.println("Item deleted: " + item);
                delete_item_field.setText(""); // Clear field after pressing enter
            }
        });  


         // *************exists item function********************************
        JLabel item_exits = new JLabel("exits_item"); //label object
        item_exits.setFont(mainFont);
        item_exits_field = new JTextField();
        item_exits_field.setFont(mainFont);  
        item_exits_field.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){
                String item = item_exits_field.getText(); // what happens when the the text is added
                boolean exists = s.item_exits(item);
                System.out.println("Item rexits: " + exists); 
                item_exits_field.setText(""); // Clear field after pressing enter
            }
        });  



        // *************rename item function********************************
        JLabel rename_item = new JLabel("item to rename"); // where the og item is going to be
        rename_item.setFont(mainFont);
        rename_item_field = new JTextField();
        rename_item_field.setFont(mainFont);

        JLabel new_item = new JLabel("new item name "); // where the new item is going to be
        new_item.setFont(mainFont);
        new_item_field = new JTextField();
        new_item_field.setFont(mainFont);
        
        
        rename_item_field.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){
                item = rename_item_field.getText(); // what happens when the the text is added
                rename_item_field.setText(""); // Clear field after pressing enter
            }
        });

        new_item_field.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){
                String new_name = new_item_field.getText(); // what happens when the the text is added
                s.rename_item(item, new_name);
                System.out.println("Item "+  item +  "is replaced with: " + new_name);
                new_item_field.setText(""); // Clear field after pressing enter
            }
        });



         // *************clear list function********************************          
        JButton clear_listButton = new JButton("clear the list");
        clear_listButton.setFont(mainFont);
        clear_listButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){
                s.clear_list();
                System.out.println("all Items deleted: " );
                
            }
        });


         // *************print list function********************************
         // this is a button
         JButton print_listButton = new JButton("print the list");
        print_listButton.setFont(mainFont);
        print_listButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){
                System.out.println("all Items printed: " );
                s.print_list();
                
            }
        }); 

        JPanel buttoPanel = new JPanel();
        buttoPanel.setLayout(new GridLayout(1, 2, 5, 5));
        buttoPanel.setOpaque(false);
        buttoPanel.add(clear_listButton);
        buttoPanel.add(print_listButton);


        

         // the panel that contains the functions
        JPanel actionsPanel = new JPanel();
        actionsPanel.setLayout(new GridLayout(10,1,5,5));
        actionsPanel.setOpaque(false);
        actionsPanel.add(add_item); // you add labels 
        actionsPanel.add(add_item_field); // and the text field
        actionsPanel.add(delete_item); // you add labels 
        actionsPanel.add(delete_item_field); // and the text field
        actionsPanel.add(item_exits); // you add labels 
        actionsPanel.add(item_exits_field); // and the text field
        actionsPanel.add(rename_item); // you add labels 
        actionsPanel.add(rename_item_field); // and the text field
        actionsPanel.add(new_item); // you add labels 
        actionsPanel.add(new_item_field); // and the text field


        // ---------------settting the panel ie putting the canvas ---------------------------
        //BorderLayout divided the interface into: north, west, est, south , centre
        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout()); // layout manager is BorderLayoutt 
        mainPanel.setBackground(new Color(222, 72, 58)); // put red like todoist
        mainPanel.setBorder(BorderFactory.createEmptyBorder(10,10,10,10));
        mainPanel.add(actionsPanel, BorderLayout.NORTH);
        mainPanel.add(buttoPanel, BorderLayout.SOUTH);

        add(mainPanel); // addthis the main panel to the class' frame
        setVisible(true); // best to call setVisible(true); as the last step after adding all components (to avoid potential rendering bugs)



        // TODO: add tests 
       
    }

    public static void main(String[] args) {
        MainFrame myFrame = new MainFrame();
        myFrame.initialize();
    }
    
}
