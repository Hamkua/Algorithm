import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    static LinkedList<Integer> CircularQueue = new LinkedList<>();


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        for(int i = 1; i <= n; i++){
            CircularQueue.add(i);
        }

        int result = 0;

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < m; i++){
            int data = Integer.parseInt(st.nextToken());
            int targetIndex = CircularQueue.indexOf(data);

             int left = targetIndex;
             int right = CircularQueue.size() - targetIndex;

             if(left < right){
                 while(CircularQueue.getFirst() != data){
                     result += 1;
                     Integer first = CircularQueue.pollFirst();
                     CircularQueue.add(first);
                 }

                 CircularQueue.pollFirst();

             }else{
                 while(CircularQueue.getFirst() != data){
                     result += 1;
                     Integer last = CircularQueue.pollLast();
                     CircularQueue.add(0, last);
                 }

                 CircularQueue.pollFirst();
             }
        }

        System.out.println(result);

    }
}
