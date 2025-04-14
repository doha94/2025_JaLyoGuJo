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
    # 리스트의 정렬 상태를 유지하면서 새 노드를 추가한다.
    def insertSorted(self, newNode):
        if self.head is None:
            self.head = newNode
            self.count = 1
        else:
            # 1. 정렬 되어있대요
            # insertFront로 값을 넣고? 이면 insertFront(Node(newNode))를 이 안에서 사용하겢?
            # 이제 받은 값을 비교하기?
            # Number = insertFront(Node(newNode))로 값을 받고 ?
            # Number를 반복해서 비교해야겠죠?
            # head -> 1000 500 100 None
            # 여기에다 300을 넣는다고 치면?
            # 300 과 1000을 비교하고
            # 300과 500을 비교하고
            # 300과 100을 비교하고
            # 300이 100보다 작으니까?
            # 300을 100 뒤에 위치시키고?
            # head -> 1000 500 300 100 None로 저장시키면?
            # 아 진짜아아아 몰겟따ㅣ;ㅣ;ㅣㅈ머; ㅣㅓ리ㅏ절ㅈ
        
        
    #---------------------------------
    # 특정 값을 가진 노드를 연결 리스트에서 제거한다.
    def remove(self, value):
        targetNode = self.find(value)# 아래에 만들었던 find를 이용하여 리스트들의 값을 미리 확인 하고, targetNode에 넣어 둠
        if targetNode is None:  # 만약 targetNode에 값이 들어가지 않는다면 이는 리스트 안에 값이 없다는것을 가리킴. 즉 더 이상 확인할 필요가 없다는 것
            return None         # 고로 None값을 반환하여 끝냄
        else:
            previous = None
            current = self.head
            while current is not targetNode:
                previous = current
                current = current.next
            
                # targetNode가 첫 번째 노드일 때 처리
            if previous is None:
                self.head = current.next  # head를 다음 노드로 설정
            else:
                previous.next = current.next  # current 노드를 제거
                # 연결 끊었으므로 targetNode를 리턴할 수 있으면 리턴
            return targetNode
        
        
        
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
# 출력하기!

print("0-------------------------------")
lst = SList()
lst2 = SList()

lst.insertFront(Node(100))
lst.insertFront(Node(200))
lst.insertFront(Node(500))
lst.insertFront(Node(1000))
lst.remove(200)
lst.showList()


print("1-------------------------------")
lst.insertFront(Node(200))
lst.showList()


print("2-------------------------------")
lst2 = lst
lst2.reverse2()

lst2.showList()
