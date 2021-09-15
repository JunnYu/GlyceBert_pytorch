from chinesebert import ChineseBertTokenizerFast, DataCollatorForChineseBERT

tokenizer = ChineseBertTokenizerFast.from_pretrained("junnyu/ChineseBERT-base")
collate_fn = DataCollatorForChineseBERT(tokenizer)
textlist = ["弗洛伊德的悲剧凸显了在美国和世界范围", "紧迫性和重要性，国际社会必须立", "那些存在严重种族主义、种族歧视", "中方对巴基斯坦开普省发"]
textlist2 = ["紧迫性和重要性，国际社会必须立", "那些存在严重种族主义、种族歧视", "中方对巴基斯坦开普省发", "弗洛伊德的悲剧凸显了在美国和世界范围"]
batch_list = [tokenizer(t1, t2) for t1, t2 in zip(textlist, textlist2)]
batch = collate_fn(batch_list)
print(batch["pinyin_ids"].shape)

"""
{'input_ids': 
tensor([[ 101, 2472, 3821,  823, 2548, 4638, 2650, 1196, 1137, 3227,  749, 1762,
         5401, 1744, 1469,  686, 4518, 5745, 1741,  102],
        [ 101, 5165, 6833, 2595, 1469, 7028, 6206, 2595, 8024, 1744, 7354, 4852,
          833, 2553, 7557, 4989,  102,    0,    0,    0],
        [ 101, 6929,  763, 2100, 1762,  698, 7028, 4905, 3184,  712,  721,  510,
         4905, 3184, 3637, 6228,  102,    0,    0,    0],
        [ 101,  704, 3175, 2190, 2349, 1825, 3172, 1788, 2458, 3249, 4689, 1355,
          102,    0,    0,    0,    0,    0,    0,    0]], device='cuda:0'), 
'token_type_ids': 
tensor([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
       device='cuda:0'), 
'attention_mask': 
tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]],
       device='cuda:0'), 
'pinyin_ids': 
tensor([[ 0,  0,  0,  0,  0,  0,  0,  0, 11, 26,  2,  0,  0,  0,  0,  0, 17, 26,
         20,  4,  0,  0,  0,  0, 30, 14,  1,  0,  0,  0,  0,  0,  9, 10,  2,  0,
          0,  0,  0,  0,  9, 10,  5,  0,  0,  0,  0,  0,  7, 10, 14,  1,  0,  0,
          0,  0, 15, 26,  4,  0,  0,  0,  0,  0, 25, 26,  1,  0,  0,  0,  0,  0,
         29, 14,  6, 19,  3,  0,  0,  0, 17, 10,  5,  0,  0,  0,  0,  0, 31,  6,
         14,  4,  0,  0,  0,  0, 18, 10, 14,  3,  0,  0,  0,  0, 12, 26, 20,  2,
          0,  0,  0,  0, 13, 10,  2,  0,  0,  0,  0,  0, 24, 13, 14,  4,  0,  0,
          0,  0, 15, 14, 10,  4,  0,  0,  0,  0, 11,  6, 19,  4,  0,  0,  0,  0,
         28, 10, 14,  2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0, 15, 14, 19,  3,  0,  0,  0,  0, 21, 20,
          4,  0,  0,  0,  0,  0, 29, 14, 19, 12,  4,  0,  0,  0, 13, 10,  2,  0,
          0,  0,  0,  0, 31, 13, 20, 19, 12,  4,  0,  0, 30,  6, 20,  4,  0,  0,
          0,  0, 29, 14, 19, 12,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
         12, 26, 20,  2,  0,  0,  0,  0, 15, 14,  4,  0,  0,  0,  0,  0, 24, 13,
         10,  4,  0,  0,  0,  0, 13, 26, 14,  4,  0,  0,  0,  0,  7, 14,  4,  0,
          0,  0,  0,  0, 29, 26,  1,  0,  0,  0,  0,  0, 17, 14,  4,  0,  0,  0,
          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0, 19, 10, 14,  4,  0,  0,  0,  0, 29, 14,
         10,  1,  0,  0,  0,  0,  8, 26, 19,  2,  0,  0,  0,  0, 31,  6, 14,  4,
          0,  0,  0,  0, 30,  6, 19,  2,  0,  0,  0,  0, 31, 13, 20, 19, 12,  4,
          0,  0, 31, 13, 20, 19, 12,  3,  0,  0, 31, 26,  2,  0,  0,  0,  0,  0,
         31, 13, 26,  3,  0,  0,  0,  0, 30, 14,  4,  0,  0,  0,  0,  0,  0,  0,
          0,  0,  0,  0,  0,  0, 31, 13, 20, 19, 12,  3,  0,  0, 31, 26,  2,  0,
          0,  0,  0,  0, 22, 14,  2,  0,  0,  0,  0,  0, 24, 13, 14,  4,  0,  0,
          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0, 31, 13, 20, 19, 12,  1,  0,  0, 11,  6,
         19, 12,  1,  0,  0,  0,  9, 26, 14,  4,  0,  0,  0,  0,  7,  6,  1,  0,
          0,  0,  0,  0, 15, 14,  1,  0,  0,  0,  0,  0, 24, 14,  1,  0,  0,  0,
          0,  0, 25,  6, 19,  3,  0,  0,  0,  0, 16,  6, 14,  1,  0,  0,  0,  0,
         21, 26,  3,  0,  0,  0,  0,  0, 24, 13, 10, 19, 12,  3,  0,  0, 11,  6,
          1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]],
       device='cuda:0')}
"""
