#=======================================
# 단순 연결 리스트 (Singly Linked list)
#=======================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return f"[{self.data}]"
#=======================================
class SList:
    def __init__(self):
        self.head = None            # SList의 첫 노드를 가리킨다.(초기 값은 빈 리스트이므로 None)
        self.count = 0              # SList에 연결된 노드의 개수(를 항상 유지한다.)
        
        
        
        
    #---------------------------
    def __len__(self):
        return self.count
    
    
    
    
    #---------------------------
    # 새로운 노드를 만들거나 노드에 값을 추가하기
    def insertFront(self, newNode):
        if self.head is None:       
            self.head = newNode
            self.count = 1
        else:
            newNode.next = self.head
            self.head = newNode
            self.count += 1
                
                
                
    #---------------------------
    # append -> 기존의 리스트 맨 뒤에 새 노드를 연결함.
    def append(self, newNode):
        if self.head is None:       # Slist가 빈 리스트인 경우
            self.head = newNode     # 추가하려는 새 노드(newNode)가 첫 노드가 된다.
            self.count = 1
        else:       # 1개 이상의 노드가 있는 경우, (마지막 노드를 찾아서 그 뒤에 newNode를 연결한다.)
            current = self.head     # 리스트의 첫 노드(self.head)부터 순서대로 확인하며 마지막 노드를 찾는다.
            while current.next is not None:     # 다음 노드가 마지막 노드가 아니라면(현재 가리키고 있는 노드의 다음이 값이 있다면)
                current = current.next          # current는 다음 노드를 가리키도록 설정.
                
            current.next = newNode
            self.count += 1
    
    
    
        
    #---------------------------------
    # 리스트의 맨 끝에 새로운 요소를 추가하기
    def appendValue(self, value):
        self.append(Node(value))
    
    
    
    
    #----------------------------     
    # 리스트 보여주기       
    def showList(self):
        print("Head->", end="")
        current = self.head
        while current is not None:
            print(f"{current}-", end="")
            current = current.next
        print(f"-> None")
        print(f"({self.count}개 노드가 있습니다.)")

    
    


    #---------------------------------
    # 리스트의 첫 노드를 삭제하며 반환한다. (빈 리스트이면 none 반환)
    def unshift(self):
        if self.head is None:
            return None
        else:
            header = self.head
            self.head = self.head.next  # 첫 노드 제거
            header.next = None
            self.count -= 1
            return header
        
        
        
        
    #---------------------------------
    # 리스트를 역순으로 출력하기.
    def reverse(self):
        revList = SList()   # 역순으로 재구성하는 데 활용할 빈 리스트 생성
        
        # 기존 리스트의 첫 노드를 차례대로 제거하며 revList에 insertFront() 처리한다.
        while self.head is not None:
            h = self.unshift()  # 기존 리스트의 첫 노드를 제거한다. (h에 저장.)
            revList.insertFront(h)  # 새 리스트(recList)의 insertFront()로 제거한 노드를 추가한다.
        
        self.head = revList.head
        self.count = revList.count
        
    
    
    
    #----------------------------------
    def reverse2(self):
        revHead = None
        while self.head is not None:
            next = self.head.next
            self.head.next = revHead
            revHead = self.head
            self.head = next
            
        self.head = revHead
    
    
    
    
    #---------------------------------
    # 정렬되지 않은 현재의 리스트를 정렬상태로 재구성한다.
    def sort(self, order="UP"):
        sorted = SList()            # 빈 리스트를 하나 만들어준다.          -> 리스트를 별도로 만들어서 옮긴 후 사용하기 위해
        # 현재 리스트의 노드를 하나씩 차례대로 꺼내서 sorted 리스트에 insertSorted로 추가한다.
        while self.count:           # while self.head is not None와 같은 말입니다. 같은데 왜 저렇게 쓰냐구요? 저도 몰라요
            sorted.insertSorted(self.unshift(), order)      # 새로 만든 빈 리스트 sorted에 원래있던 노드들 insertSorted로 넣음 (order은 UP과 DOWN으로 어떤 방식으로 정렬할것인지 정의하는것)
        
        self.head = sorted.head
        self.count = sorted.count
    
    
    
    
    #---------------------------------
    # 현재 리스트의 복사본 리스트를 생성하여 반환하기
    def copy(self):
        newList = SList()
        current = self.head
        while current:
            newList.appendValue(current.data)
            current = current.next
        return newList
    
    
    
    
    
    #---------------------------------
    # 현재 단순 연결 리스트의 파이썬 리스트 버전을 생성하여 반환한다.
    def list(self):
        newList = list()
        current = self.head
        while current:
            newList.append(current.data)
            current = current.next
        return newList    
    
    
        
    #---------------------------------
        # 리스트의 정렬 상태를 유지하면서 새 노드를 추가한다.
    def insertSorted(self, newNode, order="UP"):
        if self.head is None:
            self.head = newNode
            self.count = 1
        else:
            # 새 노드(newNode)가 삽입될 위치를 찾기 위한 준비를 한다.
            current = self.head # 새 노드보다 큰 값을 가진 노드를 차례대로 찾아가기 위한 변수 (첫 노드부터 비교 시작)
            previous = None     # current가 다음 노드로 이동할 때, 현재의 current값을 백업하며 따라간다.

            while current is not None:  # 리스트의 마지막 노드까지 비교할 예정.
                if order == "UP":
                    check = newNode.data > current.data
                else:
                    check = newNode.data < current.data

                if check:
                    previous = current
                    current = current.next
                else:
                    if previous is None:    # 첫 노드 앞에 추가되어야 하는 경우
                        newNode.next = current
                        self.head = newNode
                    else:
                        previous.next = newNode
                        newNode.next = current
                    self.count += 1
                    return
            # 리스트의 마지막에 새 노드를 연결해야 하는 경우
            previous.next = newNode
            self.count += 1



    # def insertSorted(self, newNode):
    #     if self.head is None:   
    #         self.head = newNode
    #         self.count = 1
    #     else:
    #         # 새 노드(newNode)가 삽입될 위치를 찾기위한 준비를 한다.
    #         current = self.head     # current -> 새 노드보다 큰 값을 가진 노드를 차례대로 찾아가기 위한 변수        -> 그냥 self.head를 놔두고 다른 노드를 사용하기 위해서 저장하는 역할임
    #         previous = None         # current가 다음 노드로 이동할 때, 현재의 current값을 백업하며 따라간다.
            
    #         while current is not None:  #current에 하나씩 순서대로 값을 변경하여 넣을 것이기 때문에 current에 값이 있는지 없는지로 while로 계속 반복
    #             if newNode.data > current.data:     # 만약 새로운 노드가 current에 넣었던 값(self.head)보다 크다면? 
    #                 previous = current              # previous에 current 값을 넣어주기(previous에 current(기존 값)을 백업시키기)        -> self.head가 current에 들어가 있기 때문에
    #                 current = current.next          # current에 있던 값에 current의 다음 값을 넣어주고 다시 while문 반복시키기          -> 새로운 노드의 데이터가(값이) current안에 들어간 새로운 값보다 작을 때까지

    #             else:                               # 만약 새로운 노드가 current의 값보다 작다면?
    #                 if previous is None:            # 첫 노드 앞에 추가되어야 하는 경우         -> 즉 "previous의 값이 비어있다" = "위 if문이 실행되지 않았다" 이기때문에 self.head의 값 첫번째에 들어간다는 뜻이다.
    #                                                 # -> previous의 값이 비어있는지 아닌지 확인하는 이유: 위에있던 if newNode.data > current.data의 반복이 끝나고 previous에 값이 남아있을 수 있기 때문에
    #                     newNode.next = current      # 새로운 노드에 current(self.head)를 추가시킨다.
    #                     self.head = newNode         # self.head에 새로운 노드, 연결되어있는 노드(current)들을 저장시킨다.
    #                 else:
    #                     previous.next = newNode     # 위 if문에서 끝난 previous의 다음 값에 새로운 노드를 연결시킨다.                         # 첫 노드 앞에 추가되는 경우가 아니라면?    -> "previous의 값이 비어있지 않다" = "위 if문이 실행되었다" 이기 때문에 첫 노드가 아닌 두번째 이후의 노드에 연결된다 임.
    #                     newNode.next = current      # 이후 previous -> newNode 로 연결되어있는 상태의 newNode 뒤에 current(위 if문에서 사용하지 않은 current.next들이 남아있음)를 연결시
    #                 self.count += 1                 # 새로운거 들어왔으니까 카운트 증가
    #                 return
            
        
        
    #---------------------------------
    # 특정 값을 가진 노드를 연결 리스트에서 제거한다.
    # def remove(self, value):
    #     targetNode = self.find(value)# 아래에 만들었던 find를 이용하여 리스트들의 값을 미리 확인 하고, targetNode에 넣어 둠
    #     if targetNode is None:  # 만약 targetNode에 값이 들어가지 않는다면 이는 리스트 안에 값이 없다는것을 가리킴. 즉 더 이상 확인할 필요가 없다는 것
    #         return None         # 고로 None값을 반환하여 끝냄
    #     else:
    #         previous = None
    #         current = self.head
    #         while current is not targetNode:
    #             previous = current
    #             current = current.next
            
    #             # targetNode가 첫 번째 노드일 때 처리
    #         if previous is None:
    #             self.head = current.next  # head를 다음 노드로 설정
    #         else:
    #             previous.next = current.next  # current 노드를 제거
    #             # 연결 끊었으므로 targetNode를 리턴할 수 있으면 리턴
    #        return targetNode
        
    def remove(self, node):
        if node is None:
            return None

        if node is self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
        elif node is self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        self.count -= 1
        node.next = None
        node.prev = None
        return node


        
    #---------------------------------
    # 특정값이 리스트에 포함되어 있는지 결과를 알려주기
    # 반환값: 없을 경우 None, 있으면 해당 노드 반환
    def find(self, value):
        current = self.head
        while current is not None:
            if value == current.data:
                return current
            else:
                current = current.next
        # vlaue를 찾지 못하면 while 종료
        return None
#===========================================================================================================================================================
# 5월 13일
"""
    이중 연결 리스트(double linked list)
"""


#=======================================================
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return f"[{self.data}]"
    
    
#========================================================
class DList:                    # 임의의 리스트에 연결부 만들어주기?
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
        
    #---------------------------------------------------
    # 리스트의 맨 뒤에 value 값을 가진 새 노드를 연결한다.
    def append(self, value):        # 값을 뒤에다 붙이기
        # 새로 추가할 노드 생성
        newNode = Node(value)
        # 빈 리스트인 경우를 먼저 확인하고 처리한다.
        if self.count == 0:
            self.head = newNode
            self.tail = newNode
        else:           # 빈 리스트가 아닌 경우에는 리스트의 tail이 가리키는 노드 뒤에 새 노드를 연결한다.
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        # 리스트의 노드 개수 증가 반영
        self.count += 1


    #---------------------------------------------------
    def insertFront(self, value):    # 값을 앞에다 붙이기
        newNode = Node(value)
        if self.count == 0:
            self.tail = newNode
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.count += 1
        
        
    #---------------------------------------------------
    # 리스트에서 value 값을 가진 첫 노드를 찾아서 반환한다.
    # 없으면 none 값을 반환
    def find(self, value):
        current = self.head
        while current:          # == while current is not none
            if value == current.data:
                return current
            else:
                current = current.next
        # vlaue를 찾지 못하면 while 종료
        return None        
    
    
    #---------------------------------------------------
    def showList(self):             # 리스트 보여주기
        print("head->", end="")
        # head부터 마지막 노드까지 차례대로 노드를 출력한다.
        current = self.head
        while current:      # == while current is not none
            print(current, end="-")
            current = current.next
        # 리스트의 노드 개수를 출력하면서 리스트 출력 마무리.
        print(f"({self.count} nodes)")
        
        
    #---------------------------------------------------
    # 리스트의 존재하는 target 앞에 value값을 가진 새 노드를 생성하여 삽입한다.                                                     속보! 이해안됨 지피티한테 물어보기
    def insertBefore(self, target, value):
        if target:
            return None
        if target is self.head:
            self.insertFront(value)
        else:
            newNode = Node(value)
            newNode.next = target
            newNode.prev = target.prev
            target.prev.next = newNode
            target.prev = newNode
        self.count += 1
    #---------------------------------------------------
