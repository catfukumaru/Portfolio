


public class ShoppingList{

    public String[] list = new String[100]; 
    public int length  = 0;

    public void add_item(String item){
        this.list[this.length] = item;
        this.length +=1;
    }
    public void delete_item(String item){
        for (int i = 0; i <this.list.length; i++){
            if(this.list[i] != null && this.list[i].equalsIgnoreCase(item)){
                this.list[i] = null;
            }
        }
        this.length -=1;
    }

    public boolean item_exits(String item){
        for (int i = 0; i <this.list.length; i++){
            if(this.list[i] != null && this.list[i].equalsIgnoreCase(item)){
                return true;
            }
        }
        this.length -=1;
        return false;
        
    }


    public void rename_item(String item, String new_name){
        for (int i = 0; i <this.list.length; i++){
            if(this.list[i] != null && this.list[i].equalsIgnoreCase(item)){
                this.list[i] = new_name ;
            }
        }
        
    }

     public void clear_list(){
        for (int i = 0; i <this.list.length; i++){
            this.list[i] = null; 
        }
        this.length =0;
        
    }

    public void print_list(){

        for(String el: this.list){
            if (el!=null){
                System.out.println(el);
            }
            
        }
    }


}





