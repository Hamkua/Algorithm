import java.io.*;
import java.util.*;

public class Main {
    static StringTokenizer st;
    static int n, x, y, nx, ny, cnt, sharkSize = 2, eatCnt = 0;
    static boolean isContinue = true;
    static int[][] data, visited;
    static Point currLocation;
    static Point destination;

    static int a = 0;

    static Queue<Point> queue = new LinkedList<>();

    static PriorityQueue<Point> pq = new PriorityQueue<>();
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        data = new int[n][n];
        visited = new int[n][n];
        for(int i = 0; i < n; i++){
            Arrays.fill(visited[i], -1);
        }


        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++){
                int tmp = Integer.parseInt(st.nextToken());
                if(tmp == 9){
                    visited[i][j] = 0;
//                    queue.add(new Point(i, j));
                    currLocation = new Point(i, j);
                    tmp = 0;
                }
                data[i][j] = tmp;
            }
        }


        if(check()) {
            bfs();
        }
        System.out.println(cnt);

    }

    public static void cleanVisited(){
        for(int i = 0; i < n; i++){
            Arrays.fill(visited[i], -1);
        }
        visited[currLocation.x][currLocation.y] = cnt;
    }

    public static boolean check(){

        pq.clear();
        cleanVisited();
        queue.clear();

        queue.add(new Point(currLocation.x, currLocation.y));

        while(!queue.isEmpty()){
            Point pointForCheck = queue.poll();
            int x = pointForCheck.x;
            int y = pointForCheck.y;

            for(int i = 0; i<4; i++){
                nx = x + dx[i];
                ny = y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                    if(visited[nx][ny] == -1) {
                        Point tmpPoint = new Point(nx, ny, visited[x][y] + 1);
                        if (0 < data[nx][ny] && data[nx][ny] < sharkSize) {
                            pq.add(tmpPoint);
                        } else if(data[nx][ny] == 0|| data[nx][ny] == sharkSize){
                            visited[nx][ny] = visited[x][y] + 1;
                            queue.add(tmpPoint);
                        }
                    }
                }
            }
        }

        if(pq.size() > 0) {
            cleanVisited();
            destination = pq.peek();
            queue.add(new Point(currLocation.x, currLocation.y));
//            System.out.println("destination = (" + destination.x + ", " + destination.y + ")");
            return true;
        }
        return false;
    }

    public static void bfs(){

        while(!queue.isEmpty()) {

//            try {
//                Thread.sleep(1000);
//            } catch (InterruptedException e) {
//                e.printStackTrace();
//            }
            Point point = queue.poll();
            x = point.x;
            y = point.y;

//            System.out.println("x = " + x + ", y = " + y);

//            printVisited();

            for (int i = 0; i < 4; i++) {
                nx = x + dx[i];
                ny = y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < n) {
//                    System.out.println("destination = (" + destination.x + ", " + destination.y + ")" );
//                    System.out.println("nx = " + nx + ", ny = " + ny);
//                    System.out.println("sharkSize = " + sharkSize);
//                    System.out.println("data[nx][ny] = " +data[nx][ny]);

//                    printVisited();

                    if (visited[nx][ny] == -1 && data[nx][ny] <= sharkSize) {
                        Point tmpPoint = new Point(nx, ny);

                        if(destination.equals(tmpPoint)){
                            cnt = visited[x][y] + 1;
//                            System.out.println("도착!");
//                            System.out.println("(" + nx +", " + ny + ")");
                            data[nx][ny] = 0;
                            currLocation = tmpPoint;
                            eatCnt++;
                            if(eatCnt == sharkSize){
                                sharkSize++;
                                eatCnt = 0;
                            }

                            isContinue = check();
//                            System.out.println(isContinue);
                            if(isContinue){
                                cleanVisited();
                                break;

                            }else{
//                                System.out.println("끝");
                                queue.clear();
                                break;
                            }
                        }else {
//                        System.out.println("oo");
                            visited[nx][ny] = visited[x][y] + 1;
                            queue.add(tmpPoint);
                        }
                    }

                }
            }
            if(!isContinue){
                break;
            }

        }

    }


    public static void printData(){
        System.out.println("cnt = " + cnt);
        for(int i = 0; i < n; i++){
            for(int j = 0; j<n; j++){
                System.out.print(data[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void printQueue(){
        System.out.println("queue = ");
        Iterator<Point> it = queue.iterator();
        while(it.hasNext()){
            Point next = it.next();
            System.out.print("( " + next.x + ", " + next.y + " )\t");

        }
        System.out.println();
    }

    public static void printVisited(){
        System.out.println("visited = ");
        for(int i = 0; i < n; i++){
            for(int j = 0; j<n; j++){
                System.out.print(visited[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println();
    }

    static class Point implements Comparable<Point>{
        int x, y;
        Integer visitCnt;

        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }

        public Point(int x, int y, Integer visitCnt){
            this.x = x;
            this.y = y;
            this.visitCnt = visitCnt;
        }

//        오름차순이기 때문에, 리턴값을 반대로 함
        @Override
        public int compareTo(Point point) {

            if(this.visitCnt < point.visitCnt){
                return -1;
            }else if(this.visitCnt.equals(point.visitCnt)) {
                if (this.x < point.x) {
                    return -1;
                } else if (this.x == point.x) {
                    return Integer.valueOf(this.y).compareTo(point.y);
                }
            }
            return 1;
        }

        @Override
        public boolean equals(Object obj) {
            if(obj instanceof Point){
                Point otherPoint = (Point)obj;
                if(otherPoint.x == this.x && otherPoint.y == this.y){
                    return true;
                }
            }
            return false;
        }
    }
}
