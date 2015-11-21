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
    max-width: 400px;
    margin: 5% auto;
  }

  label {
    text-decoration: none;
    list-style-type: none;
  }

  img {
    width: 30%;
  }
  </style>

  <script>
    this.stickers = opts.stickers
  </script>
</stickers>
