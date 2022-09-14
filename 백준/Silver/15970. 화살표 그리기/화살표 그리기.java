import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static Map<String, List<Integer>> map = new HashMap<>();
    static List<Integer> list;
    static int minDistance, absValue;
    static int result = 0;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        for(int i = 0; i<n; i++){
            st = new StringTokenizer(br.readLine());

            int point = Integer.parseInt(st.nextToken());
            String color = st.nextToken();

            if(map.containsKey(color)){

                list = map.get(color);

            }else{

                list = new ArrayList<>();
            }
            list.add(point);
            map.put(color, list);

        }

        ArrayList<String> keySet = new ArrayList<>(map.keySet());
        for(String key : keySet){
            list = map.get(key);
            for(int i = 0; i < list.size(); i++){
                minDistance = Integer.MAX_VALUE;
                for(int j = 0; j < list.size(); j++){
                    if(i == j)
                        continue;

                    absValue = Math.abs(list.get(i) - list.get(j));
                    if(minDistance >= absValue){
                        minDistance = absValue;
                    }

                }
                result += minDistance;

            }
        }

        System.out.println(result);

    }
}