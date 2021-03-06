# DFS & BFS 그래프 탐색 알고리즘

<br/>

## 그래프 탐색 알고리즘

---

-   탐색: 많은 양의 데이터 중 원하는 데이터를 찾는 과정
-   대표적인 탐색 알고리즘에 DFS와 BFS가 있음
-   코딩 테스트에 매우 자주 등장!

<br/>

## 그래프 탐색 알고리즘을 구현하기 위해 반드시 알고 있어야 하는 자료구조

---

### 1. 스택(선입후출): 먼저 들어온 것이 나중에 나간다, 박스 쌓기

### 2. 큐(선입선출): 먼저 들어온 것이 먼저 나간다, 터널 지나기

### 3. 재귀함수: 자기 자신을 다시 호출, 스택처럼 함수가 순서대로 쌓이는 방식

-   파이썬에서는 재귀 호출에 대한 깊이 제한이 있음
-   종료조건을 명시하는 것이 핵심!
-   모든 재귀함수는 반복문으로 구현 가능
-   컴퓨터 내부적으로 재귀함수를 스택처럼 쌓는 방식이므로, 스택을 재귀함수로 구현할 수 있음

<br/>

## DFS: Depth-First-Search

---

-   `깊이 우선 탐색`, 깊은 부분을 우선적으로 탐색하는 알고리즘
-   **Stack** 혹은 재귀함수를 이용
-   시작 노드로부터 해당 분기의 노드를 끝까지 탐색하는 방식
-   미로찾기에서 한 방향으로 갈 수 있는 최대한 나아가는 것

### 장점

-   BFS보다 적은 메모리를 사용
-   찾으려는 노드가 깊은 단계에 있는 경우 빠르게 찾을 수 있음

### 단점

-   효율적이지 못한 경우가 있음(해가 없는 경로를 탐색하게 되더라도 가장 깊은 곳까지 탐색하게 되므로)
-   DFS를 통해 얻어진 해가 최단 경로라는 보장이 없음(최초로 해를 찾아내게 되면 알고리즘을 바로 종료하므로)

<br/>

## BFS: Breadth-First-Search

---

-   `너비 우선 탐색`, 가까운 부분부터 우선적으로 탐색하는 알고리즘
-   **Queue** 이용
-   시작 노드로부터 아직 방문하지 않은 인접 노드를 순차적으로 방문하며 탐색하는 방식

### 장점

-   답이 되는 경로가 여러 개인 경우에도 **`최단경로임을 보장`**
-   깊이가 무한정 깊어진다고 하더라도 최단경로를 찾을 수 있음

### 단점

-   경로가 길어지면 메모리를 많이 필요(탐색해야 하는 노드 수가 급격히 많아지게 되므로)

<br/>

## BFS vs DFS 비교

---

![https://velog.velcdn.com/images%2Flucky-korma%2Fpost%2Fe2ef7ac3-14e6-42e7-a768-224c5f773e29%2FR1280x0-3.gif](https://velog.velcdn.com/images%2Flucky-korma%2Fpost%2Fe2ef7ac3-14e6-42e7-a768-224c5f773e29%2FR1280x0-3.gif)

<br/>

## DFS vs BFS 선택을 위한 아이디어

---

### `단순히 모든 정점을 방문하는 경우` → BFS & DFS

### `최단 거리를 구하는 문제`→ **BFS**(최단거리임을 보장)

### `이동 과정에 여러 제약이 존재하는 문제` → **DFS**

A → B로 이동하며 노드의 숫자를 저장해야하는데 경로상 같은 숫자가 있으면 안되는 조건과 같이, 각각의 경로마다 특징을 저장해둬야 하는 경우

### `검색 대상 그래프가 정말 큰 경우` → DFS 고려
