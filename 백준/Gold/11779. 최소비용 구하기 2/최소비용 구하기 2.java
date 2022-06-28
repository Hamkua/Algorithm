import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static final int INF = Integer.MAX_VALUE;
    static PriorityQueue<Node> pq = new PriorityQueue<>();
    static LinkedList[] data;
    static int[] result;
    static LinkedList[] route;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        result = new int[n + 1];
        Arrays.fill(result, INF);

        data = new LinkedList[n + 1];
        route = new LinkedList[n + 1];
        for(int i = 0; i<=n; i++){
            data[i] = new LinkedList<Node>();
            route[i] = new LinkedList<Integer>();
        }

        for(int i = 0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            int fromNode = Integer.parseInt(st.nextToken());
            int toNode = Integer.parseInt(st.nextToken());
            int edge = Integer.parseInt(st.nextToken());
            data[fromNode].add(new Node(edge, toNode));
        }

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        result[start] = 0;
        route[start].add(start);

        dijkstra(start);

        System.out.println(result[end]);
        System.out.println(route[end].size());
        Iterator it = route[end].iterator();
        while(it.hasNext()){
            System.out.print(it.next() + " ");
        }

        br.close();
    }

    static void dijkstra(int s){
        pq.add(new Node(0, s));

        while(!pq.isEmpty()){
            Node poll = pq.poll();
            int weight = poll.getWeight();
            int destination = poll.getDestination();
            if(result[destination] < weight){
                continue;
            } else{
                Iterator it = data[destination].iterator();
                while(it.hasNext()) {
                    Node nextNode = (Node) it.next();
                    int nextWeight = nextNode.getWeight();
                    int nextDestination = nextNode.getDestination();

                    int totalWeight = weight + nextWeight;
                    if(result[nextDestination] > totalWeight){
                        result[nextDestination] = totalWeight;
                        pq.add(new Node(totalWeight, nextDestination));
                        route[nextDestination] = new LinkedList<Integer>();
                        Iterator routeIt = route[destination].iterator();
                        while(routeIt.hasNext()){
                            route[nextDestination].add((Integer) routeIt.next());
                        }
                        route[nextDestination].add(nextDestination);
                    }
                }
            }
        }
    }
    static class Node implements Comparable{
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
        public int compareTo(Object o) {
            Node node = (Node)o;
            if(this.getWeight() < node.getWeight()){
                return 1;
            }else{
                return -1;
            }
        }
    }
}

