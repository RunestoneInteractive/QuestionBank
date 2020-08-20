.. mchoice:: localstore_client
   :author: bmiller
   :difficulty: 3.0
   :basecourse: webfundamentals
   :chapter: Dynamic
   :subchapter: prototype3
   :topics: Dynamic/prototype3
   :from_source: T
   :pct_on_first: 0.303030303
   :total_students_attempting: 33
   :num_students_correct: 31
   :mean_clicks_to_correct: 2.064516129

   What is the best way to arrange for our new LocalStorageSaver class to be a client of the model?
   
   - Make LocalStorageSaver a subclass of ShoppingList
   
     - No, although this could work it would tightly couple the model to a particular method of persistent storage.
   
   - Make the LocalStorage object a property of our model.
   
     - No, although we could make this work as well, it's not the best solution for our architecture.
   
   - Have the LocalStorageSaver object subscribe to the model
   
     + Corrrect!