public class main {
    public static void main(String[] args) {
        ShoppingList s = new ShoppingList();
        s.add_item("butter");
        s.add_item("milk");
        s.delete_item("milk");
        s.print_list();
    }
}