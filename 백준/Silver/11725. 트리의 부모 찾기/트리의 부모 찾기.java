import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static List<Integer>[] data;
    static Map<Integer, Integer> map = new HashMap<>();
    static int n;

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        data = new ArrayList[n + 1];
        for(int i = 0; i<n + 1; i++){
            data[i] = new ArrayList<>();
        }

        for(int i = 1; i < n; i++){
            st = new StringTokenizer(br.readLine());

            int parent = Integer.parseInt(st.nextToken());
            int child = Integer.parseInt(st.nextToken());

            data[parent].add(child);
            data[child].add(parent);

        }

        getParents(1);

        for(int i = 2; i <= n; i++){
            System.out.println(map.get(i));
        }
    }

    public static void getParents(int idx){

        Iterator<Integer> it = data[idx].iterator();
        while(it.hasNext()){
            Integer child = it.next();
//            System.out.println(child);
            if(!map.containsKey(child)){
                map.put(child, idx);
                getParents(child);
            }
        }
    }
}