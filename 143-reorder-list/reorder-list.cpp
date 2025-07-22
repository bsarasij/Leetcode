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
    ListNode* reverse(ListNode* prev, ListNode* curr){
        if (!curr){
            return prev ;
        }
        ListNode* next = curr -> next;
        curr -> next = prev;
        return reverse (curr, next);
    }
    void reorderList(ListNode* head) {
        if (!(head -> next)){
            return;
        }
        ListNode* fast = head;
        ListNode* slow = head;
        while (fast && fast -> next){
            fast = fast -> next -> next;
            slow = slow -> next;
        }
        ListNode* prev = nullptr;
        ListNode* second = reverse(prev, slow -> next);
        slow -> next = nullptr;
        ListNode* first = head;
        while (second){
            ListNode* temp1 = first->next;
            ListNode* temp2 = second->next;
            first->next = second;
            second->next = temp1;
            first = temp1;
            second = temp2;
        }
    }
};