# Simple Blog API

routes:
  - posts/                   - All posts
  - posts/{pk}               - Single post with the given primary key
  - posts/{pk}/comments/     - Comments that have been posted on a single post
  - posts/{pk}/comments/{pk} - Single comment with the given primary key
  - posts/{pk}/reviews/      - All reviews related to the post
  - posts/{pk}/reviews/{pk}  - Single review related to the post
  
