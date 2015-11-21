<stickers>
  <ul>
      <li each={ items }>
        <img src="{ path }" alt="" />
        <label>{ id }</label>
      </li>
  </ul>

  <style scoped>
  :scope {
    padding-left: 10px;
    padding-right: 10px;
  }

  li {
    display: inline-block;
    max-width: 200px;
    margin: 5% auto;
    width: 150px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    margin-left: 20px;
    margin-left: 20px;
  }

  label {
    text-decoration: none;
    list-style-type: none;
    font-size: 12px;
  }

  img {
    width: 50%;
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
  </style>

  <script>
    this.stickers = opts.stickers
  </script>
</stickers>
