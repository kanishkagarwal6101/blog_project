import React from "react";
import { FaComment, FaHeart } from "react-icons/fa";

import { Link } from "react-router-dom";

const Story = ({ story }) => {
  const editDate = (createdAt) => {
    const monthNames = [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ];
    const d = new Date(createdAt);
    var datestring =
      d.getDate() + " " + monthNames[d.getMonth()] + " " + d.getFullYear();
    return datestring;
  };

  const truncateContent = (content) => {
    const trimmedString = content.substr(0, 50);
    return trimmedString;
  };
  const truncateTitle = (title) => {
    const trimmedString = title.substr(0, 40);
    return trimmedString;
  };

  return (
    <div className="story-card">
      <Link to={`/story/${story.slug}`} className="story-link">
        <img className=" story-image" src={story.image} alt={story.title} />
        <div className="story-content-wrapper">
          <h5 className="story-title">
            {story.title.length > 15
              ? truncateTitle(story.title) + "..."
              : story.title}
          </h5>

          <div style={{ display: "flex", justifyContent: "space-between", padding:"5px 0px" }}>
            <div style={{ display: "flex" }}>
              <div>
                <b className="likeCount" style={{ padding: "5px" }}>
                  <FaHeart color="rgb(99, 99, 99)" />
                </b>
                {story.likeCount}
              </div>
              <div>
                <b className="commentCount" style={{ padding: "5px" }}>
                  <FaComment color="rgb(99, 99, 99)" />
                </b>
                {story.commentCount}
              </div>
            </div>
            <div>
              <b0
                className="readtime"
                style={{
                  padding: "5px",
                }}
              >
                {story.readtime}m read
              </b0>
            </div>
          </div>
          <p className="story-createdAt">{editDate(story.createdAt)}</p>

        </div>
      </Link>
    </div>
  );
};

export default Story;