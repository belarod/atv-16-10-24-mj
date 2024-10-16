class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None  # Referência para o topo da pilha
        self.length = 0  # Contador para acompanhar o length da pilha

    def __str__(self):
        valores = []
        current = self.top
        while current:
            valores.append(str(current.value))
            current = current.next
        return " -> ".join(valores)

    def push(self, value):
        new_node = Node(value)  # Criando um novo nó com o valor
        new_node.next = self.top  # O novo nó aponta para o nó que era o topo
        self.top = new_node  # O novo nó se torna o topo da pilha
        self.length += 1  # Incrementa o length da pilha

    def pop(self):
        if self.is_empty():
            return None
        value = self.top.value  # Armazena o valor do nó que está no topo
        self.top = self.top.next  # Atualiza o topo para o próximo nó
        self.length -= 1  # Decrementa o length da pilha
        return value

    def is_empty(self):
        return self.top is None

    def top_item(self):
        if self.is_empty():
            return None
        return self.top.value

    def stack_length(self):
        count = 0
        current = self.top
        while current: #enquanto current n for nulo, passa p prox
            count += 1
            current = current.next
        return count


stack = Stack()
stack.push(10)
stack.push(5)
stack.push(30)
stack.push(30)
stack.push(30)
stack.push(30)

print(stack.stack_length())