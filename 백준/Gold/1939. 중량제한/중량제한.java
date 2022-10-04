import java.io.*;
import java.util.*;

public class Main {
    static final int INF = Integer.MAX_VALUE;
    static int n, m, a, b, c, start;
    static String end;
    static List<Node>[] data;

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        data = new ArrayList[n + 1];
        for(int i = 0; i< n + 1; i++){
            data[i] = new ArrayList<>();
        }

        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());

            data[a].add(new Node(-1 * c, b));
            data[b].add(new Node(-1 * c, a));
        }

        st = new StringTokenizer(br.readLine());

        start = Integer.parseInt(st.nextToken());
        end = st.nextToken();

        System.out.println(dijkstra());
    }

    static int dijkstra(){

        boolean[] visited = new boolean[n + 1];
        visited[start] = true;

        Map<String, Integer> result = new HashMap<>();
        for(int i = 0; i<n+1; i++){
            if(i == start){
                result.put(Integer.toString(start), 0);
            }else {
                result.put(Integer.toString(i), INF);
            }
        }
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(-1 * INF, start));

        while(!pq.isEmpty()){
            Node node = pq.poll();
            int prevEdge = node.edge;
            int prevDestination = node.destination;

//            System.out.println(prevDestination);
            if(result.get(Integer.toString(prevDestination)) < prevEdge){
//                System.out.println("daw");
                continue;
            }else{


                for(int i = 0; i < data[prevDestination].size(); i++){
                    int nextEdge = data[prevDestination].get(i).edge;
                    int nextDestination =  data[prevDestination].get(i).destination;

                    int minEdge = Math.max(nextEdge, prevEdge);

                    String nextDestinationKey = Integer.toString(nextDestination);
                    if(minEdge < result.get(nextDestinationKey)){
                        result.put(nextDestinationKey, minEdge);
                        pq.add(new Node(minEdge, nextDestination));
                    }
                }
            }
        }

        return -1 * result.get(end);
    }

    static class Node implements Comparable<Node>{
        int edge, destination;

        public Node(int edge, int destination){
            this.edge = edge;
            this.destination = destination;
        }

        @Override
        public int compareTo(Node n) {
            return this.edge - n.edge;

        }
    }
}

