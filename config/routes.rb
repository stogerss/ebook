Ebook::Application.routes.draw do
  get "home/index", :as => 'index'
  
  root :to => 'home#index'

end
