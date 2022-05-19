import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static LinkedList<Integer> queue = new LinkedList<>();
    static int count = 0;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] strings = br.readLine().split(" ");
        int n = Integer.parseInt(strings[0]);
        int m = Integer.parseInt(strings[1]);

        String[] strings2 = br.readLine().split(" ");
        int[] dataArr = new int[m];

        for(int i = 0; i<dataArr.length; i++){
            dataArr[i] = Integer.parseInt(strings2[i]);
        }

        for(int i =1; i<n+1; i++){
            queue.add(i);
        }

        for(int data : dataArr){
            while(true){
                int peek = queue.peek();
                if(peek == data){
                    queue.poll();
                    break;
                }

                if(queue.size() - queue.indexOf(data) > queue.indexOf(data)){
                    int q = queue.poll();
                    queue.add(q);
                    count++;

                }else{
                    int q = queue.pollLast();
                    queue.addFirst(q);
                    count++;

                }
            }
        }
        System.out.println(count);
        br.close();
    }
}
