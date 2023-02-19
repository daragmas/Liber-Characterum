Rails.application.routes.draw do
  resources :passions
  resources :races
  resources :specialist_skills
  resources :skills
  resources :armors
  resources :traits
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
end
