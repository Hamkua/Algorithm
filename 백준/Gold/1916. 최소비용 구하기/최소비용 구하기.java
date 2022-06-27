import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static PriorityQueue<Node> pq = new PriorityQueue<Node>();
    static LinkedList[] data;
    static int[] result;
    static boolean[] visited;
    static final int INF = Integer.MAX_VALUE;
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        data = new LinkedList[n + 1];
        result = new int[n + 1];
        visited = new boolean[n + 1];
        for(int i = 0; i < n+1; i++){
            data[i] = new LinkedList<Node>();
            result[i] = INF;
        }

        for(int i = 0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            int fromNode = Integer.parseInt(st.nextToken());
            int toNode = Integer.parseInt(st.nextToken());
            int edge = Integer.parseInt(st.nextToken());

            data[fromNode].add(new Node(edge, toNode));
        }

        st = new StringTokenizer(br.readLine());
        int startNode = Integer.parseInt(st.nextToken());
        int endNode = Integer.parseInt(st.nextToken());

        dijkstra(startNode);
        System.out.println(result[endNode]);

        br.close();
    }

    static void dijkstra(int start){
        pq.add(new Node(0, start));

        while(!pq.isEmpty()){
            Node poll = pq.poll();
            if(result[poll.getDestination()] < poll.getWeight()){
                continue;
            }


            Iterator it = data[poll.getDestination()].iterator();
            while(it.hasNext()){
                Node next = (Node)it.next();
                int next_weight = poll.getWeight() + next.getWeight();
                if(result[next.getDestination()] > next_weight){
                    result[next.getDestination()] = next_weight;
                    pq.add(new Node(next_weight, next.getDestination()));
                }
            }
        }
    }

    static class Node implements Comparable<Node>{
        private int weight, destination;

        public Node(int weight, int destination){
            this.weight = weight;
            this.destination = destination;
        }

        public int getWeight() {
            return weight;
        }

        public int getDestination() {
            return destination;
        }

        @Override
        public int compareTo(Node o) {
            if(this.getWeight() < o.getWeight()){
                return 1;
            }else{
                return -1;
            }
        }
    }
}