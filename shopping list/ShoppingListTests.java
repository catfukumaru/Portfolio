import static org.junit.Assert.*;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;



public class ShoppingListTests {
    @Test
    public void add_item_test(){
        ShoppingList test_list = new ShoppingList();
        test_list.add_item("mango");
        assertEquals("mango", test_list.list[0]);

    }


    @Test
    public void delete_item_test(){
        ShoppingList test_list = new ShoppingList();
        test_list.add_item("mango");
        test_list.delete_item("mango");
        assertEquals(null, test_list.list[0]);

    }

     @Test
    public void item_exits_test(){
        ShoppingList test_list = new ShoppingList();
        test_list.add_item("mango");
        boolean bool_val =test_list.item_exits("mango");
        assertEquals(true, bool_val);
    }


     @Test
    public void rename_item_test(){
        ShoppingList test_list = new ShoppingList();
        test_list.add_item("mango");
        test_list.rename_item("mango", "banana");
        assertEquals("banana", test_list.list[0]);
    }

     @Test
    public void clear_list_test(){
        ShoppingList test_list = new ShoppingList();
        test_list.add_item("mango");
        test_list.clear_list();
        assertEquals(null, test_list.list[0]); //
    }


    @Test // TODO: something is wrong here
    public void testPrintList() {
        // Arrange
        ShoppingList s = new ShoppingList();
        s.add_item("apple");
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        PrintStream oldOut = System.out;
        System.setOut(new PrintStream(outputStream));

        // Act
        s.print_list();

        // Restore original System.out
        System.setOut(oldOut);

        // Assert
        String expected = s.list[0];
        assertEquals(expected, outputStream.toString());
    }









}
