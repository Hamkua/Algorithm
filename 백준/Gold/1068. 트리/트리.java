import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static int count = 0;
    static int num = 0;
    static Tree root;
    static Tree[] trees;
    static Integer remove;
    static int rootIndex = 0;
    static LinkedList<Integer>[] data;

    static class Tree{
        private Integer value;
        private Tree[] link = new Tree[2];

        public Tree(Integer value) {
            this.value = value;
        }

        public static void delete(int index){
            if(index != remove) {
                if(data[index].isEmpty()){
                    count++;
                }
                else {
                    Iterator<Integer> iterator = data[index].iterator();
                    while (iterator.hasNext()) {
                        int child = iterator.next();
                        if (child != remove) {
                            delete(child);
                        }
                    }
                }
            }

        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        trees = new Tree[n];
        for(int i = 0; i<n; i++){
            trees[i] = new Tree(i);
        }

        data = new LinkedList[n];
        for(int i = 0; i<n; i++){
            data[i] = new LinkedList<>();
        }
        String[] strings = br.readLine().split(" ");

        remove = Integer.parseInt(br.readLine());

        for(int i = 0; i<n; i++){
            num = Integer.parseInt(strings[i]);
            if(num == -1){
                root = trees[i];
                rootIndex = i;
            }else{
                if(remove != i) {
                    data[num].add(i);
                }
            }
        }

        Tree.delete(rootIndex);
        System.out.println(count);
        br.close();
    }
}