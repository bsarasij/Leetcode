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
    ListNode* recurse(ListNode* prev, ListNode* curr){
        if (curr == nullptr){
            return prev;
        }
        ListNode* next = curr -> next;
        curr -> next = prev;
        return recurse(curr, next);
    }
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr || head -> next == nullptr){
            return head;
        }
        ListNode* prev = nullptr;
        return recurse(prev, head);
         
    }
};