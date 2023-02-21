public class SkipListTest {
    
    public static void main(String[] args) {
        SkipList<Entry> myList = new SkipList<>();
        myList.put(120000, "Biking");
        myList.put(120001, "Cycling");
        myList.remove(120000);
        myList.remove(120001);
        //System.out.println(myList.get(120000).element.value);
        System.out.println(myList.head.down.down.next.element.getValue());
    }
}
