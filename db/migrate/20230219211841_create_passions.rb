class CreatePassions < ActiveRecord::Migration[7.0]
  def change
    create_table :passions do |t|
      t.string :name
      t.string :type
      t.json   :characteristic_bonus
      t.json   :characteristic_penalty
      t.string :description
      t.string :special
      t.timestamps
    end
  end
end
