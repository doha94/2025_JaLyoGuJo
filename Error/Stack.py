#---------------------------------------------------
# 이중연결 리스트를 이용하여 스택(STack)구한하기
#---------------------------------------------------
from PythonStudng import * 
#---------------------------------------------------
class StackUnderFlow(Exception):
    pass


class Stack(DList):
    # 스택에 새 데이터를 추가하는 연산
    def push(self, value):
        self.insertFront(value)
    
    
    
    # 스택에 맨 위에있는 데이터를 가져우는 연산( 맨 위의 데이터는 스택에서 제거됨)
    def pop(self):
        if self.isEmpty():
            raise StackUnderFlow("Stack Empty!!")
        else:
            returnValue = self.head.data
            self.remove(self.head)
            return returnValue
    
    
    
    # 스택이 비었는지를 확인하는 연산
    def isEmpty(self):
        if self.count == 0:
            return True                                                                                                                                                                                                                                                                                                                                                                     
        return False
    
    
    
    # 스택에서 TOP 항목의 값을 읽어오는 연산(읽은 항목이 제거되지 않음. pop() 비교)
    def peek(self):
        return self.head
    
    
    
    # 괄호의 짝이 맞는지 확인하는 함수
    # 교수님 답변
    def checkParenthese(self, st):
        pleft = "(<{["
        pright = ")>}]"
        pairs = "()<>{}[]"

        for item in st:
            if item in pleft:
                self.push(item)
            elif item in pright:
                try:
                    top = self.pop()
                except StackUnderFlow:
                    print(f"닫는 괄호 {item}에 대응되는 여는 괄호가 없습니다.")
                    return False
                if (top + item) in pairs:
                    continue
                else:
                    print(f"매치 오류 발생: {top}, {item}")
                    return False
            else:
                continue

        if not self.isEmpty():
            print("닫히지 않은 괄호가 남아 있습니다.")
            return False
        else:
            return True
    
#---------------------------------------------------------------------------------
stack = Stack()
stack.checkParenthese("[][p[][]]][]")
