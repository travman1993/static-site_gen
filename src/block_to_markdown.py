def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    
    cleaned_blocks = [block.strip() for block in blocks if block.strip()]
    
    final_blocks = []
    for block in cleaned_blocks:
        sub_blocks = block.split('\n')
        final_blocks.extend([sub_block.strip() for sub_block in sub_blocks if sub_block.strip()])
    
    return final_blocks