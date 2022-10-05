import java.io.*;
import java.util.*;

public class Main {

    static Tree root;
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while(true){
            try{
                String input = br.readLine();
                if(input == null || input.equals("")){
                    throw new MyException();
                }

                Tree.insert(new Tree(Integer.parseInt(input)));


            }catch (MyException e){
                Tree.postOrder(root);
                break;
            }
        }


    }

    static class MyException extends Exception{ }

    static class Tree{
        int value;
        Tree parent, left, right;

        public Tree(int value){
            this.value = value;
        }

        public static void postOrder(Tree node){
            if(node != null){
                postOrder(node.left);
                postOrder(node.right);
                System.out.println(node.value);
            }
        }

        public static void insert(Tree child){
            if(root == null){
                root = child;
            }else {
                Tree parentNode = null;
                Tree node = root;
                while (node != null) {
//                    System.out.print(node.value + ", ");
                    parentNode = node;

                    if (node.value > child.value) {

                        node = node.left;

                    }else{
                        node = node.right;


                    }
                }
//                System.out.println();
                if(parentNode.value > child.value){
                    parentNode.left = child;
                }else{
                    parentNode.right = child;
                }
            }
        }
    }
}

