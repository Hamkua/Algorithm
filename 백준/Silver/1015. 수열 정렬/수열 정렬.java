import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static Map<String, List<Integer>> map = new HashMap<>();
    static LinkedList<Integer> list;
    static String key;
    static int[] data;
    static int[] sortedData;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        data = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i<n; i++){
            data[i] = Integer.parseInt(st.nextToken());
        }

        sortedData = data.clone();
        Arrays.sort(sortedData);
        for(int i = 0; i<n; i++){
            key = Integer.toString(sortedData[i]);
            if(!map.containsKey(key)){
                list = new LinkedList<>();

            }else{
                list = (LinkedList<Integer>)map.get(key);
            }
            list.add(i);
            map.put(key, list);
        }

        for(int idx : data){
            LinkedList<Integer> list = (LinkedList<Integer>) map.get(Integer.toString(idx));
            sb.append(list.poll()).append(" ");
        }
        System.out.println(sb);
    }
}