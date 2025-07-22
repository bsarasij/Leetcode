/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode();
        dummy -> next = head; 
        ListNode* node1 = dummy;
        ListNode* node2 = dummy;
        int counter = 0;
        while (node1){
            if (counter > n ){
                node2 = node2 -> next;
            }
            node1 = node1 -> next ;
            counter = counter + 1; 
        }
        ListNode* temp = node2 -> next;
        node2 -> next = node2 -> next -> next;
        delete temp;
        ListNode* newHead = dummy -> next;
        delete dummy;
        return newHead;
    }
};